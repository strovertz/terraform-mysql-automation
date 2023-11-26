<?php

namespace App\Models;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;
use Carbon\Carbon;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;



/**
 * @property Carbon $deleted_at
 * @property Carbon $created_at
 * @property string $nome
 * @property float $valor
 * @property string $tipo_servico
 * @property string $endereco
 * @property string $descricao
 * @property mixed $data
 */

class Supplier extends Model
{
    use HasApiTokens, HasFactory, Notifiable, SoftDeletes;

    public $primaryKey = 'id';

    public $table = 'servicos';
    public $fillable = [
        'nome',
        'data',
        'valor',
        'descricao',
        'endereco',
        'tipo_servico',
    ];

    protected $hidden = [
        'created_at',
        'deleted_at',
    ];

    public $casts = [
        'created_at' => 'datetime:d-m-Y',
        'deleted_at' => 'datetime:d-m-Y',
    ];
}
